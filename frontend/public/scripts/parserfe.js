/* Parser Front End - Javascript  File */

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
            <label className="sr-only" for="patentNumber">Patent Publication Number</label>
            <input type="text" class="form-control" id="patentNumber" 
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

ReactDOM.render(
  <SearchForm/>,
  document.getElementById('searchbar')
);