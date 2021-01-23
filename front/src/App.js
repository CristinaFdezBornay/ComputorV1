import React from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import ComputorV1 from './pages/ComputorV1';
import Header from './components/Header';

function App() {
    return (
        <React.Fragment>
            <CssBaseline/>
                <Header/>
                <ComputorV1/>
        </React.Fragment>
    )
}

export default App;