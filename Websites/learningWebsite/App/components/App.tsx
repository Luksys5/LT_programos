import * as React from 'react';
var $ = require("jquery");

class App extends React.Component<any, any> {
  constructor(){
    super();
    this.state= {
      returnData: {}
    }
  }

  componentDidMount() {
    $("#POSTForm").submit(function(e: any){
      (function(){
        var worker = new Worker("./workJob.js");
        worker.onmessage = function(evt: any) {
          console.log(evt.data);
        }
        worker.onerror = function(msg) {
          console.log(msg);
        }
        worker.postMessage("");
      })();

      $.ajax({
        type: "POST",
        url: "http://localhost:8080/WebService1.asmx/getNameById",
        cache: false,
        contentType: "application/x-www-form-urlencoded",
        dataType: "json",
        data: $(this).serialize(),
        success: function(data: any) {
          console.log("GET succeed");
          console.log(data);
        },
        failure: function(msg: any) {
          console.log(msg);
        }
      });
      e.preventDefault();
    });   
  }

  private createWorker() {
    
  }


  render() {
    const {returnData} = this.state;    
    return (
      <form id="POSTForm">
          Id: <input type='text' name='id' id='id'/>
          <input type="submit" value="Submit"/>  
      </form>
    );  
}
}

export default App;
