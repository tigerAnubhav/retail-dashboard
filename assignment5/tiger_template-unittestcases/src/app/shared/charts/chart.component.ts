import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-charts',
  templateUrl: './chart.component.html',
})
export class ChartComponent  {
  private myChart: any = null;
  @Input() chartData:any;
  @Input() chartType = '';
  constructor() {}
}