import React, { useState } from 'react';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import ButtonGroup from '@material-ui/core/ButtonGroup';

const useStyles = makeStyles((theme) => ({
    root: {
      flexGrow: 1,
      textAlign: 'center',
      backgroundColor: '#ccebff',
      padding: '3vh',
      borderRadius: '3%'
    },
}));

export default function Calculator(props) {
    const classes = useStyles();

    const [inputCalculator, setInputCalculator] = useState('');
    const setInputAndChangeComponent = () => {
        props.setInput(inputCalculator)
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
                <Grid item md={8}>
                <ButtonGroup
                        size='large'
                        fullWidth={true}
                        color='primary'
                        orientation='vertical'
                        variant='outlined'
                    >
                        <ButtonGroup orientation='horizontal'>
                            <Button>{' + '}</Button>
                            <Button>{' - '}</Button>
                        </ButtonGroup>
                        <ButtonGroup orientation='horizontal'>
                            <Button>{' 1 '}</Button>
                            <Button>{' 2 '}</Button>
                            <Button>{' 3 '}</Button>
                        </ButtonGroup>
                        <ButtonGroup orientation='horizontal'>
                            <Button>{' 4 '}</Button>
                            <Button>{' 5 '}</Button>
                            <Button>{' 6 '}</Button>
                        </ButtonGroup>
                        <ButtonGroup orientation='horizontal'>
                            <Button>{' 7 '}</Button>
                            <Button>{' 8 '}</Button>
                            <Button>{' 9 '}</Button>
                        </ButtonGroup>
                        <ButtonGroup orientation='horizontal'>
                            <Button>{' << '}</Button>
                            <Button>{' 0 '}</Button>
                            <Button>{' AC '}</Button>
                        </ButtonGroup>
                    </ButtonGroup>
                </Grid>
                <Grid item md={4}>
                    <ButtonGroup
                        size='large'
                        fullWidth={true}
                        color='primary'
                        orientation='vertical'
                        variant='contained'
                    >
                        <Button>{' no exp '}</Button>
                        <Button>{' * x '}</Button>
                        <Button>{' * x² '}</Button>
                        <Button>{' = '}</Button>
                    </ButtonGroup>
                </Grid>
                <Grid item md={12}>
                    <Button
                        variant='contained'
                        color='primary'
                        onClick={setInputAndChangeComponent}>
                        <Typography variant='h6'>
                            {'RESULT'}
                        </Typography>
                    </Button>
                </Grid>
            </Grid>
        </div>
    )
}
