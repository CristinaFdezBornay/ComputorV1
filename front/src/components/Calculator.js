import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Numbers from './Numbers';
import Exponents from './Exponents';
import SendResult from './SendResult';

const useStyles = makeStyles(() => ({
    root: {
      flexGrow: 1,
      textAlign: 'center',
      backgroundColor: '#ccebff',
      padding: '3vh',
      borderRadius: '5%'
    },
}));

export default function Calculator(props) {
    const classes = useStyles();
    const [inputCalculator, setInputCalculator] = useState('');
    const setInputAndChangeComponent = () => {
        let finalInput = inputCalculator.replaceAll('*x²', '*X^2').replaceAll('*x', '*X^1')
        if (finalInput.split('=').length - 1 === 0)
            finalInput += '= 0'
        else if (finalInput.split('=').length - 1 > 1)
            finalInput = 'INPUT ERROR'
        props.setInput(finalInput)
        props.changeComponent()
    }

    return (
        <div className={classes.root}>
            <Grid container spacing={2} alignItems='center' justify='center'>
                <Grid item md={12}>
                    <Typography variant='h4' color='primary'>
                        {inputCalculator ? inputCalculator : 'Do something thanks'}
                    </Typography>
                </Grid>
                <Numbers
                    inputCalculator={inputCalculator}
                    setInputCalculator={setInputCalculator}
                />
                <Exponents
                    inputCalculator={inputCalculator}
                    setInputCalculator={setInputCalculator}
                />
                <SendResult
                    title='RESULT'
                    onClick={setInputAndChangeComponent}
                />
            </Grid>
        </div>
    )
}
