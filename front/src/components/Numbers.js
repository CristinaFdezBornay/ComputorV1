import React from 'react';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import ButtonGroup from '@material-ui/core/ButtonGroup';

export default function Numbers(props) {
    return (
        <Grid item md={8}>
            <ButtonGroup
                size='large'
                fullWidth={true}
                color='primary'
                orientation='vertical'
                variant='outlined'
            >
                <ButtonGroup orientation='horizontal'>
                    {[' + ', ' - '].map(sign => 
                        <Button key={sign} onClick={() => {
                            props.setInputCalculator(props.inputCalculator+sign)
                        }}>{sign}</Button>
                    )}
                </ButtonGroup>
                <ButtonGroup orientation='horizontal'>
                    {['1', '2', '3'].map(number => 
                        <Button key={number} onClick={() => {
                            props.setInputCalculator(props.inputCalculator+number)
                        }}>{number}</Button>
                    )}
                </ButtonGroup>
                <ButtonGroup orientation='horizontal'>
                    {['4', '5', '6'].map(number => 
                        <Button key={number} onClick={() => {
                            props.setInputCalculator(props.inputCalculator+number)
                        }}>{number}</Button>
                    )}
                </ButtonGroup>
                <ButtonGroup orientation='horizontal'>
                    {['7', '8', '9'].map(number => 
                        <Button key={number} onClick={() => {
                            props.setInputCalculator(props.inputCalculator+number)
                        }}>{number}</Button>
                    )}
                </ButtonGroup>
                <ButtonGroup orientation='horizontal'>
                    <Button onClick={() => {
                            props.setInputCalculator(props.inputCalculator+'.')
                        }}>{'.'}</Button>
                    <Button onClick={() => {
                            props.setInputCalculator(props.inputCalculator+'0')
                        }}>{'0'}</Button>
                    <Button onClick={() => {
                            props.setInputCalculator('')
                        }}>{' AC '}</Button>
                </ButtonGroup>
            </ButtonGroup>
        </Grid>
    )
}
