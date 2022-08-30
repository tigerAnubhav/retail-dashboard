
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
  selector: 'app-bar-chart',
  templateUrl: './bar-chart.component.html',
  styleUrls: ['./bar-chart.component.scss'],
})
@UntilDestroy()
export class BarChartComponent implements OnInit {
  @Input() chartUrl = '';
  @Input() chartData :any;
  _chartOption: EChartsOption = {};
  private showLegend: boolean = true;
  x:OptionDataValue[];
  y:OptionDataValue[];

  constructor(private _httpClient: HttpClient,private dashser:DashboardService) {}

  ngOnInit() {
    console.log('Hi',this.chartData)
    this.loadChart(this.chartData['x'],this.chartData['y'])

  }

  private loadChart(x: any,y:any): void {
    this._chartOption = {

      grid: { containLabel: true },
      xAxis: {
        type: 'category',
        boundaryGap: true,
        data:[
          "Wing G",
          "Stretch 4",
          "Combo G",
          "C",
          "PF/C",
          "Scoring PG",
          "Wing F",
          "Pure PG"
      ],
        axisLabel:{
          show:true,

        }
      },
      yAxis: {
        type: 'value',
        axisLabel:{
          show:true,
        }
      },
      visualMap: {
        orient: 'horizontal',
        left: 'center',

        // Map the score column to color
        dimension: 0,

        color: ['#65B581']
      },

      series: [
        {
          data: [
            175,
            62,
            82,
            161,
            92,
            36,
            108,
            7
        ],
          type: 'bar',
        },
      ],
    };
  }
}