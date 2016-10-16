/* Parser Front End - Javascript  File */

var PatentParser = React.createClass({
    getInitialState: function() {
        return {
                    claim: {words:[]},
                    number: ""
                };
    },
    loadClaimFromServer: function(number) {
        this.setState({number: number});
        $.ajax({
            url: '/api/claimdata' + '/' + number,
            dataType: 'json',
            cache: false,
            success: function(data) {
                console.info(data);
                this.setState({claim: data.claim});
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(status, err.toString());
            }.bind(this)
        });
    },
    render: function() {
        return (
            <div>
                <div id="searchbar" className="row text-center">
                    <SearchForm onSearchSubmit={this.loadClaimFromServer}/>
                </div>
                <div className="row">
                    <Claim words={this.state.claim.words}/>
                </div>
            </div>
        );
    }
});

var SearchForm = React.createClass({
    getInitialState: function() {
        return {patentNumber: ''};
    },
    handleSubmit: function(e) {
        e.preventDefault();
        if (!this.state.patentNumber) {
            return;
        }
        this.props.onSearchSubmit(this.state.patentNumber);
    },
    handleNumberChange: function(e) {
        this.setState({patentNumber: e.target.value});
    },
    render: function() {
        return (
          <form className="searchForm form-inline" onSubmit={this.handleSubmit}>
            <div className="form-group">Enter patent publication number to search:</div>
            <div className="form-group">
                <label className="sr-only" htmlFor="patentNumber">Patent Publication Number</label>
                <input type="text" className="form-control" id="patentNumber" 
                    placeholder="e.g. EP3029606"
                    value={this.state.patentNumber}
                    onChange={this.handleNumberChange}
                />
            </div>
            <button className="btn btn-default" value="Search">Search</button>
          </form>
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
  <PatentParser/>,
  document.getElementById('content')
);
