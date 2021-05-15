import {Card, Spin, Typography} from "antd";
import React from "react";

const WaitSecondPlayer = () => {
    return (
        <Card title={<Typography>Идёт поиск второго игрока</Typography>}
              bordered={true}
              style={{margin: "auto"}}
        >
            <Spin size="large"/>
        </Card>
    )
}

export default WaitSecondPlayer
