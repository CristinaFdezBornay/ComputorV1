import React from 'react';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

export default function SendResult(props) {
    return (
        <Grid item md={12}>
            <Button
                variant='contained'
                color='primary'
                onClick={() => {props.onClick()}}>
                <Typography variant='h6'>
                    {props.title}
                </Typography>
            </Button>
        </Grid>
    )
}
