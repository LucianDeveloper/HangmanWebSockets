import React, {useState} from "react";
import {Layout, Typography, Card, Row, Col} from "antd";
const {Footer, Content} = Layout;


const Button = ({onCLick, level, char, color}) => {
    return (
        <Col onClick={onCLick}>
            <Card>
                <Typography.Title level={level} type={color}>
                    {char}
                </Typography.Title>
            </Card>
        </Col>
    )
}


const isCorrectChar = (char, correctChars) => correctChars.includes(char)
const isIncorrectChar = (char, correctChars, usedChars) => (!correctChars.includes(char) && usedChars.includes(char))


const KeyboardGame = ({
      onSelectChar,
      correctChars= [],
      usedChars = [],
   }) => {
    const keyboard = Array.from('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ').map((char) => {
        const color = isCorrectChar(char, correctChars) ? 'success' :
            (isIncorrectChar(char, correctChars, usedChars) ? 'danger' : 'default')
        return <Button onCLick={() => onSelectChar(char)}
                       level={3}
                       char={char}
                       color={color}
        />
    })

    const symbols = correctChars.map((char) => {
        return <Button onCLick={null}
                       level={1}
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
                </Row>
            </Footer>
        </Layout>
    )
}


export default KeyboardGame