import { Component, OnInit } from '@angular/core';
import { AlertService } from './alert.service';
import { Alert } from './alert.model'; // Import the Alert model if you haven't already

@Component({
    selector: 'app-alert',
    templateUrl: './alert.component.html',
    styleUrls: ['./alert.component.css']
})
export class AlertComponent implements OnInit {
    alerts: Alert[] = []; // Initialize the alerts property

    constructor(private alertService: AlertService) { }

    ngOnInit() {
        this.alertService.getAlerts().subscribe({
            next: (data: any) => { // Change the type of data to 'any'
                if (Array.isArray(data)) { // Check if data is an array
                    this.alerts = data as Alert[]; // Cast data to Alert[] if it's an array
                } else {
                    console.error('Received data is not an array:', data);
                }
            },
            error: (error) => {
                console.error('An error occurred:', error);
            },
            complete: () => {
                console.log('Alerts subscription completed.');
            }
        });
    }
}

