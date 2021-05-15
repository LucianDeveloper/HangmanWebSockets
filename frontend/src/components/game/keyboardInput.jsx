import React, {useState} from "react";
import {Layout, Typography, Card, Row, Col} from "antd";
import {DoubleLeftOutlined, DeleteOutlined, CheckOutlined} from "@ant-design/icons";
const {Footer, Content} = Layout;


const Button = ({onCLick, level, char}) => {
    return (
        <Col onClick={onCLick}>
            <Card>
                <Typography.Title level={level}>
                    {char}
                </Typography.Title>
            </Card>
        </Col>
    )
}


const KeyboardInput = ({onSet}) => {
    const [word, setWord] = useState('');

    const symbols = Array.from(word).map((char) => {
        return <Button onCLick={null}
                       level={1}
                       char={char}
        />
    })

    const keyboard = Array.from('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ').map((char) => {
        return <Button onCLick={() => setWord(word + char)}
                       level={3}
                       char={char}
        />
    })

    return (
        <Layout>
            <Content style={{height: '120px'}}>
                <Row justify="center">{symbols}</Row>
            </Content>
            <Footer>
                <Row justify="center">
                    {keyboard.slice(0, 12)}
                </Row>
                <Row justify="center">
                    {keyboard.slice(12, 25)}
                </Row>
                <Row justify="center">
                    {keyboard.slice(25, 33)}
                    <Button onCLick={() => setWord(word.slice(0, word.length - 1))}
                            level={3}
                            char={<DoubleLeftOutlined />}
                    />
                    <Button onCLick={() => setWord("")}
                            level={3}
                            char={<DeleteOutlined />}
                    />
                    <Button onCLick={() => onSet(word)}
                            level={3}
                            char={<CheckOutlined style={{color: 'green'}}/>}
                    />
                </Row>
            </Footer>
        </Layout>
    )
}


export default KeyboardInput