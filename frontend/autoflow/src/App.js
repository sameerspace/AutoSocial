import './App.css';

import { useState } from 'react';
import { Button } from 'react-bootstrap';

function App() {

  return (
    <body>
      <h1>AutoSocial</h1>
      <form action='http://127.0.0.1:8000/post_image' encType='multipart/form-data' method='post'>
        <input name='caption' type="text" />
        <input name="files" type="file" multiple />
        <input type="submit" placeholder='Post' />
      </form>
    </body>
  );

}

export default App;
