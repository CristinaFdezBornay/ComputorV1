import React, { useState } from 'react';
import Calculator from './Calculator';
import Result from './Result';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles((theme) => ({
  root: {
      flexGrow: 1,
  },
  container: {
      backgroundColor: '#cfe8fc',
  }
}));

export default function ComputorV1() {
  const classes = useStyles();
  const [showCalculator, setShowCalculator] = useState(true)
  const [input, setInput] = useState(false)

  const changeComponent = () => { setShowCalculator(!showCalculator) }

  return (
    <Container maxWidth='lg' className={classes.container}>
      { showCalculator
        ? <Calculator
          setInput={setInput}
          changeComponent={changeComponent}
          />
          : <Result
            input={input}
            setInput={setInput}
            changeComponent={changeComponent}
          />
      }
    </Container>
  )
}