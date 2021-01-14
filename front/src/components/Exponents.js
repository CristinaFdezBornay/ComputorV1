import React from 'react';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import ButtonGroup from '@material-ui/core/ButtonGroup';

export default function Exponents(props) {
    return (
        <Grid item md={4}>
            <ButtonGroup
                size='large'
                fullWidth={true}
                color='primary'
                orientation='vertical'
                variant='contained'
            >
                {['*x', '*x²', ' = '].map(exponent => 
                    <Button key={exponent} onClick={() => {
                        props.setInputCalculator(props.inputCalculator+exponent)
                    }}>{exponent}</Button>
                )}
            </ButtonGroup>
        </Grid>
    )
}
