/* Parser Front End - Javascript  File */

// We then just use the np number as the index
var Colors = {
    aqua: "#00ffff",
    azure: "#f0ffff",
    beige: "#f5f5dc",
    black: "#000000",
    blue: "#0000ff",
    brown: "#a52a2a",
    cyan: "#00ffff",
    darkblue: "#00008b",
    darkcyan: "#008b8b",
    darkgrey: "#a9a9a9",
    darkgreen: "#006400",
    darkkhaki: "#bdb76b",
    darkmagenta: "#8b008b",
    darkolivegreen: "#556b2f",
    darkorange: "#ff8c00",
    darkorchid: "#9932cc",
    darkred: "#8b0000",
    darksalmon: "#e9967a",
    darkviolet: "#9400d3",
    fuchsia: "#ff00ff",
    gold: "#ffd700",
    green: "#008000",
    indigo: "#4b0082",
    khaki: "#f0e68c",
    lightblue: "#add8e6",
    lightcyan: "#e0ffff",
    lightgreen: "#90ee90",
    lightgrey: "#d3d3d3",
    lightpink: "#ffb6c1",
    lightyellow: "#ffffe0",
    lime: "#00ff00",
    magenta: "#ff00ff",
    maroon: "#800000",
    navy: "#000080",
    olive: "#808000",
    orange: "#ffa500",
    pink: "#ffc0cb",
    purple: "#800080",
    violet: "#800080",
    red: "#ff0000",
    silver: "#c0c0c0",
    white: "#ffffff",
    yellow: "#ffff00",
    key: function(n) {
        return this[Object.keys(this)[n]];
    }
};


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
                //console.info(data);
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
                <Word text={word.word} pos={word.pos} key={word.id} np={word.np}/>
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
                    <span style={{ backgroundColor: Colors.key(this.props.np) }}>{this.props.text}</span>
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
