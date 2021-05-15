import {Card, Spin, Typography} from "antd";
import React from "react";

const WaitSetWord = () => {
    return (
        <Card title={<Typography>Подождите, сейчас второй игрок загадает слово!</Typography>}
              bordered={true}
              style={{margin: "auto"}}
        >
            <Spin size="large"/>
        </Card>
    )
}

export default WaitSetWord
