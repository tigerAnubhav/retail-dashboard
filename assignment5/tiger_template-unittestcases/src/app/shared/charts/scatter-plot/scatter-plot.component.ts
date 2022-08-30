
import { HttpClient } from '@angular/common/http';
import { Component, Injectable, Input, OnChanges, OnDestroy, OnInit, SimpleChanges } from '@angular/core';
import { EChartsOption } from 'echarts';
import { Subscription, tap, withLatestFrom } from 'rxjs';
import { map, Observable } from 'rxjs';
import { UntilDestroy, untilDestroyed } from '@ngneat/until-destroy';
import { BehaviorSubject } from 'rxjs';
import { DashboardService } from 'src/app/features/dashboard/dashboard.service';
declare type OptionDataValue = string | number | Date;

@Component({
  selector: 'app-scatter-plot',
  templateUrl: './scatter-plot.component.html',
  styleUrls: ['./scatter-plot.component.scss'],
})
@UntilDestroy()
export class ScatterPlotComponent implements OnInit {
  @Input() chartUrl = '';
  @Input() chartData :any;
  _chartOption: EChartsOption = {};
  private showLegend: boolean = true;
  x:OptionDataValue[];


  constructor(private _httpClient: HttpClient,private dashser:DashboardService) {}

  ngOnInit() {
    console.log('Hi',this.chartData)
    this.loadChart(this.chartData['x'])

  }

  private loadChart(x: any): void {
    this._chartOption =  {
      grid: {
         right:'15%',
         width:'78%'
      },
      xAxis: {
        name: 'Min / Game',
        scale: true
      },
      yAxis: {
        name: 'Points',
        scale: true
      },
      series: [

        {
          type: 'scatter',
          // prettier-ignore
          data: x
        }
      ]
    };
  }
}