import React, { useState } from 'react';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Grid from '@material-ui/core/Grid';

export default function Calculator(props) {

    const [inputCalculator, setInputCalculator] = useState('');

    const setInputAndChangeComponent = () => {
        props.setInput(inputCalculator)
        props.changeComponent()
    }

    return (
        <Grid>
            <TextField
            fullWidth={true}
            variant="outlined"
            onChange={event => {
                event.preventDefault();
                setInputCalculator(event.target.value);
            }}
            />
            <br/>
            <Button onClick={setInputAndChangeComponent}>
                We are on the Calculator - Click to change to the Result
            </Button>
        </Grid>
    )
}
