import {Col, Layout, notification, Row, Spin} from 'antd'
import KeyboardInput from "./keyboardInput";
import React from "react";
import {useState, useEffect} from "react";
import api from "../../utils/api";
import WaitSecondPlayer from "./wait_second_player";
import Disconnect from "./disconnect";
import WaitSetWord from "./wait_set_word";
import KeyboardGame from "./keyboardGame";
import SvgHangman from "./svg_hangman";
import GameResult from "./game_result";
const { Footer, Content, Sider } = Layout;


const Game = () => {
    const [websocket, setWebsocket] = useState(null);
    const [gameVars, setGameVars] = useState(null)
    useEffect(
        () => {
            const ws = new WebSocket('ws://127.0.0.1:8000/ws')
            setWebsocket(ws)
        },
        []
    );

    useEffect(
        () => {
            if (websocket !== null)
                websocket.addEventListener('message', (e) => {
                    setGameVars(JSON.parse(e.data))
                })
        }, [websocket]
    )

    let renderedElement = null;
    if (gameVars === null)
        renderedElement = <Spin />
    else {
        let inside;
        if (!gameVars.is_run)
            if (gameVars.is_disconnect)
                inside = (
                    <Disconnect onReload={() => {
                        const ws = new WebSocket('ws://127.0.0.1:8000/ws')
                        setWebsocket(ws)
                    }}/>
                )
            else
                inside = <WaitSecondPlayer />
        else {
            if (gameVars.wait_word)
                if (gameVars.you_player)
                    inside = <WaitSetWord />
                else
                    inside = (
                        <Footer>
                            <KeyboardInput onSet={(word) => {
                                const newGameVars = {...gameVars, word: word}
                                setGameVars(newGameVars)
                                websocket.send(JSON.stringify(newGameVars))
                            }}/>
                        </Footer>
                    )
            else {
                if (gameVars.you_player)
                    inside = (
                        <Footer>
                            <KeyboardGame correctChars={gameVars.answer}
                                          usedChars={gameVars.used_chars}
                                          onSelectChar={
                                              (gameVars.is_finish) ?
                                                  (char) => null
                                                  :
                                                  (char) => {
                                                      const newGameVars = {...gameVars, new_char: char}
                                                      websocket.send(JSON.stringify(newGameVars))
                                                  }
                                          }
                            />
                        </Footer>
                    )
                else
                    inside = (
                        <Footer>
                            <KeyboardGame correctChars={gameVars.answer}
                                          usedChars={gameVars.used_chars}
                                          onSelectChar={(char) => null}
                            />
                        </Footer>
                    )
                let content = null
                if (gameVars.is_finish)
                    content = <GameResult lifes={gameVars.lifes} word={gameVars.word}/>
                inside = (
                    <Row>
                        <Col style={{height: '380px', width: '400px'}}>
                            <SvgHangman lifes={gameVars.lifes}/>
                        </Col>
                        <Col>
                            <Content style={{height: '160px'}}>
                                {content}
                            </Content>
                            {inside}
                        </Col>
                    </Row>
                )
            }
        }
        renderedElement = (
            <Layout>
                {inside}
            </Layout>
        )
    }
    return renderedElement
}


export default Game
