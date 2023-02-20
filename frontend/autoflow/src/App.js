import './App.css';


function App() {

  return (
    <body>
      <h1 className='align-middle m-4'>AutoSocial</h1>
      <form action='http://127.0.0.1:8000/post_image' encType='multipart/form-data' method='post'>
        <div class="m-4 form-group">
          <label for="cap">Caption</label>
          <input type="text" class="w-50 form-control" id="cap" aria-describedby="emailHelp" placeholder="Enter caption" accept=".jpg, .jpeg, .png" />
          <small id="emailHelp" class="form-text text-muted">Include any hashtags as well</small>
        </div>
        <div className="m-4 form-group">
          <label for="exampleFormControlFile1">Images to upload</label>
          <br></br>
          <input type="file" className="form-control-file" id="exampleFormControlFile1" multiple />
        </div>
        <button type="submit" className="w-25 m-4 btn btn-primary">Post</button>
      </form>
    </body>
  );

}

export default App;
