import React from "react";
import {Result} from "antd";
import {SmileOutlined, FrownOutlined} from "@ant-design/icons";


const GameResult = ({lifes, word}) => {
    const isDone = (lifes !== 0)
    return (
        <Result
            icon={isDone ? <SmileOutlined /> : <FrownOutlined />}
            title={isDone ? `Ура! Слово "${word}" разгадано!` : `Оуч... Это же было слово "${word}"...`}
        />
    )
}


export default GameResult
