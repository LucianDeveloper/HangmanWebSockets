import {Layout} from 'antd'
import Keyboard from "./keyboard";
const { Footer, Content, Sider } = Layout;

const Game = () => {


    return (
        <Layout>
            <Sider theme='light'>

            </Sider>
            <Content>

            </Content>

            <Footer>
                <Keyboard />
            </Footer>
        </Layout>
    )
}


export default Game
