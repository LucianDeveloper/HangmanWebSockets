import React, {useState} from "react";
import {Layout, Typography, Card, Row, Col} from "antd";
import {DoubleLeftOutlined, DeleteOutlined} from "@ant-design/icons";
const {Footer, Content} = Layout;


const createButton = (onCLick, level, char) => {
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


const Keyboard = () => {
    const [word, setWord] = useState('');

    const symbols = Array.from(word).map((char) => {
        return createButton(null, 1, char)
    })

    const keyboard = Array.from('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ').map((char) => {
        return createButton(() => setWord(word + char), 3, char)
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
                    {createButton(() => setWord(word.slice(0, word.length - 1)), 3, <DoubleLeftOutlined />)}
                    {createButton(() => setWord(''), 3, <DeleteOutlined />)}
                </Row>
            </Footer>
        </Layout>
    )
}


export default Keyboard