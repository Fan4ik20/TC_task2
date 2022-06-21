import React from 'react';
import { Link } from 'react-router-dom';
import arch from './arch.png';
import bober from './bober.jpg';
import cat from './cat.jpg';

export default () => {
  return (
    <div>
      <Link to="/">Go back home</Link>
      <br />
      Zrealizowane Zadanie 2 z przedmotu Technologii Chmurowe"
      <br />
      Mark Zaianchkovskyi
      <br />
      Został zmodyfikowany server pod warunki zadania i cod był przepisany na język Python
      <br />
      Backend nie używa nginx. Niestety nie poradziłem z tym.
      <br />
      I dodany bober
      <br />
      <img src={bober} alt="bober"></img>
      <br />
      <img src={cat} alt="cat"></img>
      <img src={arch} alt="arch" />
    </div>
  );
};
