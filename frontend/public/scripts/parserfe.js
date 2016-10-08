/* Parser Front End - Javascript  File */

var SearchForm = React.createClass({
    handleSubmit: function(e) {
        e.preventDefault();
        alert("Submit");
    },
    render: function() {
    return (
      <form className="searchForm" onSubmit={this.handleSubmit}>
        <p>Enter patent publication or application number to search:
        <input
          type="text"
          placeholder="e.g. EP1111111.1"
          /*value={this.state.patentNumber}
          onChange={this.handleNumberChange}*/
        />
        </p>
        <input type="submit" value="Search" />
      </form>
    );
  }
});

ReactDOM.render(
  <SearchForm/>,
  document.getElementById('searchbar')
);