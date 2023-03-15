import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { NetworkService } from './network.service';
import { lastValueFrom } from 'rxjs';
import Chart from 'chart.js/auto';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  @ViewChild('chartCanvas')
  chartCanvas?: ElementRef<HTMLCanvasElement>;
  currentWeather: any;
  airPollution: any;
  forecast: any;

  constructor(private networkService: NetworkService) {}

  ngOnInit(): void {
    this.getData();
  }

  async getData() {
    this.currentWeather = await lastValueFrom(
      this.networkService.getCurrentWeather()
    );
    this.airPollution = await lastValueFrom(
      this.networkService.getAirPollution()
    );
    this.forecast = await lastValueFrom(this.networkService.getForecast());

    if (this.chartCanvas != undefined && this.forecast != undefined) {
      console.log(this.forecast.pm10);
      this.getChart(this.chartCanvas.nativeElement);
    }
  }

  async getChart(element: HTMLCanvasElement) {
    new Chart(element, {
      type: 'bar',
      data: {
        labels: this.forecast.date,
        datasets: [
          {
            label: 'PM10 μg/m3 by hour',
            data: this.forecast.pm10,
          },
        ],
      },
    });
  }
}
