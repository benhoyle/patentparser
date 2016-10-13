/* Parser Front End - Javascript  File */

/* Test Data */
var wordstest = [
    {
        id: 1,
        pos: "DT",
        word: "A"
    },
    {
        id: 2,
        pos: "NN",
        word: "decoding"
    },
    {
        id: 3,
        pos: "NN",
        word: "system"
    },
    {
        id: 4,
        pos: ",",
        word: ","
    },
    {
        id: 5,
        pos: "VBG",
        word: "comprising"
    },
    {
        id: 6,
        pos: ":",
        word: ":"
    }];


var SearchForm = React.createClass({
    handleSubmit: function(e) {
        e.preventDefault();
        alert("Submit");
    },
    render: function() {
    return (
      <form className="searchForm form-inline" onSubmit={this.handleSubmit}>
        <div className="form-group">Enter patent publication number to search:</div>
        <div className="form-group">
            <label className="sr-only" htmlFor="patentNumber">Patent Publication Number</label>
            <input type="text" className="form-control" id="patentNumber" 
                placeholder="e.g. EP3029606"
                /*value={this.state.patentNumber}
                onChange={this.handleNumberChange}*/
            />
        </div>
        <button className="btn btn-default" value="Search">Search</button>
      </form>
    );
  }
});

var ClaimBox = React.createClass({
    getInitialState: function() {
        return {words: []};
    },
    componentDidMount: function() {
        $.ajax({
            url: this.props.url,
            dataType: 'json',
            cache: false,
            success: function(data) {
                this.setState({words: data.words});
                console.info(this.props.url, data);
                console.info(wordstest);
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    render: function() {
        return (
            <div className="claimBox">
                <Claim words={this.state.words}/>
            </div>
        );
    }
});

var Claim = React.createClass({
    
    render: function() {
        var wordNodes = this.props.words.map(function(word) {
            return (
                    <Word text={word.word} pos={word.pos} key={word.id}/>
            );
        });
        return (
            <div className="claim row">
                {wordNodes}
            </div>
        );
    }
});

var Word = React.createClass({
    
    render: function() {
        return (
            <div className="word col-xs-4 col-sm-3 col-md-2 col-lg-1">
                <div className="row text-center lead">
                    <span>{this.props.text}</span>
                </div>
                <div className="row">
                    <span>
                        <select className="form-control">
                            <option value="one">{this.props.pos}</option>
                            <option value="two">Two</option>
                            <option value="three">Three</option>
                            <option value="four">Four</option>
                            <option value="five">Five</option>
                        </select>
                    </span>
                </div>
            </div>
        );
    }
});

ReactDOM.render(
  <SearchForm/>,
  document.getElementById('searchbar')
);

ReactDOM.render(
  <ClaimBox url={"/api/claimdata"}/>,
  document.getElementById('content')
);