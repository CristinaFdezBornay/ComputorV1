import React, { useState, useEffect } from 'react';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';

export default function Result(props) {
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
                console.log(response)
                setResult(response)
            })
            .catch( error => {
                console.log(error);
            });
        }
        fetchResult();
    }, [props.input])

    const clearInputAndChangeComponent = () => {
        props.setInput('')
        props.changeComponent()
    }

    return (
        <Grid>
            {result.reducedForm}
            <br/>
            <Button onClick={clearInputAndChangeComponent}>
                We are on the Result - Click to change to the Calculation
            </Button>
        </Grid>
    )
}