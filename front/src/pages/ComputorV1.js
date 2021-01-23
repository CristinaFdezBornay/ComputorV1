import React, { useState } from 'react';
import Calculator from '../components/Calculator';
import Result from '../components/Result';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles(() => ({
  container: {
    flexGrow: 1,
    padding: '3vh',
  }
}));

export default function ComputorV1() {
  const classes = useStyles();
  const [showCalculator, setShowCalculator] = useState(true)
  const [input, setInput] = useState(false)

  const changeComponent = () => { setShowCalculator(!showCalculator) }

  return (
    <Container className={classes.container} maxWidth='md' fixed>
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