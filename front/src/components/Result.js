import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import SendResult from './SendResult';

const useStyles = makeStyles(() => ({
    root: {
      flexGrow: 1,
      textAlign: 'center',
      backgroundColor: '#ccebff',
      padding: '3vh',
      borderRadius: '3%'
    },
}));

export default function Result(props) {
    const classes = useStyles();
    const [result, setResult] = useState({})

    useEffect(() => {
        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Request-Headers': 'Content-Type',
            },
            mode: 'cors',
            body: JSON.stringify({ rawEquation: props.input })
        }
        async function fetchResult() {
            await fetch('http://localhost:5000/api/', requestOptions)
            .then( async(responsePetition)  => {
                const response = await responsePetition.json()
                setResult(response)
            })
            .catch(() => {
                setResult({error: 'ERROR'})
            });
        }
        fetchResult();
    }, [props.input])

    const clearInputAndChangeComponent = () => {
        props.setInput('')
        props.changeComponent()
    }

    return (
        <div className={classes.root}>
            <Grid container spacing={2} alignItems='center' justify='center'>
                <Grid item md={12}>
                    <Typography variant='h4' color='primary'>
                        {'Do something thanks'}
                    </Typography>
                </Grid>
                <SendResult
                    title='GO BACK TO CALCULATION'
                    onClick={clearInputAndChangeComponent}
                />
            </Grid>
        </div>
    )
}