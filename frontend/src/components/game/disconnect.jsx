import {Button, Card, Typography} from "antd";
import React from "react";


const Disconnect = ({onReload}) => {
    return (
        <Card title={<Typography>К сожалению второй игрок вышел из игры!</Typography>}
              bordered={true}
              style={{margin: "auto"}}
        >
            <Button type="primary"
                    block
                    onClick={onReload}
            >
                Вернуться к поиску игры!
            </Button>
        </Card>
    )
}

export default Disconnect