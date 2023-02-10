const OriginalForm = () => {

    return (
        <div className="App">
            <header className="App-header">
                <h1>Auto Social</h1>
                <form>
                    <h4>Enter Caption</h4>
                    <input name="caption" type="text"></input>
                    <br></br>
                    <input onChange={fileChangedHandler} name="files" type="file" multiple />
                    <br></br>
                </form>

                <Button variant='success' onClick={handleSubmit} >Click Me</Button>
            </header>
        </div>
    );

}