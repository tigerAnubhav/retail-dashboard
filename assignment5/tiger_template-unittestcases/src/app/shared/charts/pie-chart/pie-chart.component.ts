import { Component, OnInit, Input } from '@angular/core';
import { dataTool, EChartsOption } from 'echarts';
import { DashboardService } from 'src/app/features/dashboard/dashboard.service';
declare type OptionDataValue = string | number | Date;

@Component({
  selector: 'app-pie-chart',
  templateUrl: './pie-chart.component.html',
  styleUrls: ['./pie-chart.component.scss'],
})

export class PieChartComponent implements OnInit {
  @Input() chartUrl = '';
  @Input() chartData :any;
  _chartOption: EChartsOption = {};
  x:OptionDataValue[];

  constructor(private dashser:DashboardService) {

  }

  ngOnInit() {
    this.loadChart(this.chartData['x'])
  }

  private loadChart(x : any): void {

    this._chartOption = {
      tooltip: {
        trigger: 'item'
      },
      legend: {
        orient: 'vertical',
        left: 'left'
      },
      series: [
        {
          name: 'Pie Chart',
          type: 'pie',
          radius: '80%',
          data: x,
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          }
        }
      ]
    };
  }
}