import { Component, Input, OnInit } from '@angular/core';
import { DashboardService } from 'src/app/features/dashboard/dashboard.service';
import { EChartsOption } from 'echarts';
import { UntilDestroy } from '@ngneat/until-destroy';
import { HttpClient } from '@angular/common/http';

declare type OptionDataValue = string | number | Date;

@Component({
  selector: 'app-box-plot',
  templateUrl: './box-plot.component.html',
  styleUrls: ['./box-plot.component.scss']
})
@UntilDestroy()
export class BoxPlotComponent implements OnInit {
  @Input() chartUrl = '';
  @Input() chartData :any;
  _chartOption: EChartsOption = {};
  x:OptionDataValue[];
  y:OptionDataValue[];

  constructor(private _httpClient: HttpClient, private dashser:DashboardService) {}

  ngOnInit(): void {
    console.log('Box plot data', this.chartData)
    this.loadChart(this.chartData['x'], this.chartData['y'])
  }
  private loadChart(x: any, y: any): void {
    this._chartOption = {

            dataset: [
        {
          // prettier-ignore
          source: y
        },
        {
          transform: {
            type: 'boxplot',
            config: { itemNameFormatter: function (params) {
              return x[params.value];
      } }
          }
        },
        {
          fromDatasetIndex: 1,
          fromTransformResult: 1
        }
      ],
      tooltip: {
        trigger: 'item',
        axisPointer: {
          type: 'shadow'
        }
      },

      grid: {
        left: '10%',
        right: '10%',
        bottom: '15%'
      },
      xAxis: {
        type: 'category',
        boundaryGap: true,
        nameGap: 50,
        splitArea: {
          show: false
        },
        splitLine: {
          show: false
        }
      },
      yAxis: {
        type: 'value',
        splitArea: {
          show: true
        }
      },
      series: [
        {
          name: 'boxplot',
          type: 'boxplot',
          datasetIndex: 1
        },
        {
          name: 'outlier',
          type: 'scatter',
          datasetIndex: 2
        }
      ]
    }
  }

}
