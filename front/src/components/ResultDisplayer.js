import React from 'react';
// import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
// import ButtonGroup from '@material-ui/core/ButtonGroup';

export default function ResultDisplayer(props) {
    const result = props.result
    return (
        <Grid item md={12}>
            <Typography variant='h4' color='primary'>
                {result.rawEquation}
            </Typography>
            <Typography variant='h5' color='primary'>
                {'Reduced form\t\t: '+result.reducedForm}
            </Typography>
            <Typography variant='h5' color='primary'>
                {'Polynomial degree\t: '+result.degree}
            </Typography>
            <Typography variant='h5' color='primary'>
                {result.info}
            </Typography>
            { result.root1_r !== 'null' && result.root1_i !== 'null'?
                <Typography variant='h5' color='primary'>
                    {'x₁:\t'+result.root1_r+result.root1_i+'i'}
                </Typography>
                :
                <></>
            }
            { result.root1_r !== 'null' && result.root1_i === 'null'?
                <Typography variant='h5' color='primary'>
                    {'x₁:\t'+result.root1_r}
                </Typography>
                :
                <></>
            }
            { result.root1_r === 'null' && result.root1_i !== 'null'?
                <Typography variant='h5' color='primary'>
                    {'x₁:\t'+result.root1_i+'i'}
                </Typography>
                :
                <></>
            }
            { result.root2_r !== 'null' && result.root2_i !== 'null'?
                <Typography variant='h5' color='primary'>
                    {'x₂:\t'+result.root2_r+result.root2_i+'i'}
                </Typography>
                :
                <></>
            }
            { result.root2_r !== 'null' && result.root2_i === 'null'?
                <Typography variant='h5' color='primary'>
                    {'x₂:\t'+result.root2_r}
                </Typography>
                :
                <></>
            }
            { result.root2_r === 'null' && result.root2_i !== 'null'?
                <Typography variant='h5' color='primary'>
                    {'x₂:\t'+result.root2_i+'i'}
                </Typography>
                :
                <></>
            }
        </Grid>
    )
}