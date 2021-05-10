import React from 'react';
import {Layout, Button, Space} from 'antd';
import {useHistory, useLocation} from 'react-router-dom';
const {Header, Content} = Layout;

const AdminLayout = ({email, children}) => {
    const history = useHistory();
    const location = useLocation();

    return (
        <Layout className="vh-100">
            <Header className="d-flex justify-content-between align-items-center">
                <div className="" />
                <div>
                    <Space size="large">
                        <span className="text-white fw-500">{email}</span>
                        <Button
                            type="primary"
                            onClick={() => {
                                history.push('/login');
                            }}
                        >
                            Выход
                        </Button>
                    </Space>
                </div>
            </Header>
            <Layout className="h-auto">
                <Layout className="p-4 overflow-x-hidden overflow-y-auto">
                    <Content className="p-2">
                        {children}
                    </Content>
                </Layout>
            </Layout>
        </Layout>
    );
};

export default AdminLayout;