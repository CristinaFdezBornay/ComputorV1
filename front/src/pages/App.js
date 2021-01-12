import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Container from '@material-ui/core/Container';
import ComputorV1 from '../components/ComputorV1';
import Header from '../components/Header';

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    container: {
        backgroundColor: '#cfe8fc',
    }
}));

function App() {
    const classes = useStyles();

    return (
        <React.Fragment>
            <CssBaseline />
                <Header/>
                <Container maxWidth='lg' className={classes.container}>
                    <ComputorV1/>
                </Container>
        </React.Fragment>
    )
}

export default App;