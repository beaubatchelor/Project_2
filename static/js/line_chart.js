import React, { Component } from 'react';

d3.json("/scatter_data",
    function(month_data){
        let layout = {
            title : "Product Line Sales by Month",
            margin : { t : 0}
        };
    Plotly.plot("lineChart", month_data, layout);
    }
);

class Card extends Component {
  constructor() {
    super();
    
    this.state = {
      showMenu: false,
    };
    
    this.showMenu = this.showMenu.bind(this);
    this.closeMenu = this.closeMenu.bind(this);
  }
  
  showMenu(event) {
    event.preventDefault();
    
    this.setState({ showMenu: true }, () => {
      document.addEventListener('click', this.closeMenu);
    });
  }
  
  closeMenu() {
    this.setState({ showMenu: false }, () => {
      document.removeEventListener('click', this.closeMenu);
    });
  }

  render() {
    return (
      <div>
        <button onClick={this.showMenu}>
          Show menu
        </button>
        
        {
          this.state.showMenu
            ? (
              <div className="menu">
                <button> Menu item 1 </button>
                <button> Menu item 2 </button>
                <button> Menu item 3 </button>
              </div>
            )
            : (
              null
            )
        }
      </div>
    );
  }
}