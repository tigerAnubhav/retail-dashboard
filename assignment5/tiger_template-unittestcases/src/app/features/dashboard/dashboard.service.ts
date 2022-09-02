import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, tap } from 'rxjs';
import { ActivatedRoute, Router } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
export class DashboardService {

  /**
   * Constructor
   */
  constructor(private _httpClient: HttpClient,private router:Router,private ar:ActivatedRoute) {}

  // -----------------------------------------------------------------------------------------------------
  // @ Accessors
  // -----------------------------------------------------------------------------------------------------

  // -----------------------------------------------------------------------------------------------------
  // @ Public methods
  // -----------------------------------------------------------------------------------------------------


  // getBarChartOneDta():Observable<any>{
  //   console.log('Hi I am here in getBar1')
  //   return this._httpClient.get<{x:string[],y:number[]}>('http://localhost:5000/barchartone');
  // }
  getBoxPlot():Observable<any>{
    console.log('Hi I am here in getBar')
    return this._httpClient.get<{x:string[],y:number[]}>('http://localhost:5000/boxplot');
  }
  getBarChart():Observable<any>{
    console.log('Hi I am here in getBar')
    return this._httpClient.get<{x:string[],y:number[]}>('http://localhost:5000/countplot');
  }
  getPieChart():Observable<any>{
    console.log('Hi I am here in getPie')
    return this._httpClient.get<{x:{'value':number,'name':string}[]}>('http://localhost:5000/piechart');
  }
  getScatterPlot():Observable<any>{
    console.log('Hi I am here in getScatter')
    return this._httpClient.get<{x:{'value':number,'name':string}[]}>('http://localhost:5000/scatterplot');
  }

}