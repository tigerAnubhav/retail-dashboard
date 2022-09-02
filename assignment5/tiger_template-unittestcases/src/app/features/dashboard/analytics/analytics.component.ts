import {
  ChangeDetectionStrategy,
  Component,
  OnDestroy,
  OnInit,
  ViewEncapsulation,
} from '@angular/core';
import { Router } from '@angular/router';
import { Subject, takeUntil } from 'rxjs';

import { DashboardService } from '../dashboard.service';

@Component({
  selector: 'analytics',
  templateUrl: './analytics.component.html',
  encapsulation: ViewEncapsulation.None,
})
export class AnalyticsComponent implements OnInit, OnDestroy {
  data: any;
  // barChart1Data! :{x:string[],y:number[]}
  boxPlotData! :{x:string[], y:number[]}
  barChartData! :{x:string[],y:number[]}
  pieChartData! :{x:{'value':number,'name':string}[]};
  scatterChartData! :{x:{'value':number,'value1':number}[]};
  areaCharts = ['first', 'second', 'third', 'fourth'];
  private _unsubscribeAll: Subject<any> = new Subject<any>();

  /**
   * Constructor
   */
  constructor(
    private _dashboardService: DashboardService,
    private _router: Router
  ) {}

  // -----------------------------------------------------------------------------------------------------
  // @ Lifecycle hooks
  // -----------------------------------------------------------------------------------------------------

  /**
   * On init
   */
  async ngOnInit() {

    console.log('previous',this.boxPlotData)
    this._dashboardService.getBoxPlot().subscribe((res:any)=>{
      this.boxPlotData=res;
      console.log('boxplotdata', this.boxPlotData)
    })
    console.log('previous',this.barChartData)
    this._dashboardService.getBarChart().subscribe((res:any)=>{
      this.barChartData=res;
      console.log('barchartdata',this.barChartData)
    })
    console.log('previous',this.pieChartData)
    this._dashboardService.getPieChart().subscribe((res:any)=>{
      this.pieChartData=res;
      console.log('piechartdata',this.pieChartData)
    })
    console.log('previous',this.scatterChartData)
    this._dashboardService.getScatterPlot().subscribe((res:any)=>{
      this.scatterChartData=res;
      console.log('scatterplotdata',this.scatterChartData)
    })
  }


  /**
   * On destroy
   */
  ngOnDestroy(): void {
    // Unsubscribe from all subscriptions
    this._unsubscribeAll.next(null);
    this._unsubscribeAll.complete();
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Public methods
  // -----------------------------------------------------------------------------------------------------

  /**
   * Track by function for ngFor loops
   *
   * @param index
   * @param item
   */
  trackByFn(index: number, item: any): any {
    return item.id || index;
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Private methods
  // -----------------------------------------------------------------------------------------------------

  /**
   *
   * @param element
   * @private
   */
}