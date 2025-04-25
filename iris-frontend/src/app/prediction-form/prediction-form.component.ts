import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

interface PredictionResponse {
  prediction: string;
} 

@Component({
  selector: 'app-prediction-form',
  imports: [
    CommonModule,
    FormsModule,
  ],
  templateUrl: './prediction-form.component.html',
  styleUrl: './prediction-form.component.css'
})
export class PredictionFormComponent {
  private apiUrl = 'http://127.0.0.1:8000/predict';

  sepal_l: number | null = null;
  sepal_w: number | null = null;
  petal_l: number | null = null;
  petal_w: number | null = null;

  predictionResult: string | null = null;
  isLoading = false;
  errorMessage: string | null = null;

  constructor(private http: HttpClient) {}

  onSubmit(): void {
    if (this.sepal_l === null || this.sepal_w === null || this.petal_l === null || this.petal_w === null) {
        this.errorMessage = "Please fill in all fields.";
        return;
    }

    this.isLoading = true;
    this.predictionResult = null;
    this.errorMessage = null;

    const features = {
      sepal_l: this.sepal_l,
      sepal_w: this.sepal_w,
      petal_l: this.petal_l,
      petal_w: this.petal_w
    };

    this.http.post<PredictionResponse>(this.apiUrl, features).subscribe({
      next: (response) => {
        this.predictionResult = response.prediction;
        this.isLoading = false;

        console.log('Prediction Result:', this.predictionResult);
        console.log('Image path:', `assets/img/${this.predictionResult}.png`);
      },
      error: (error) => {
        console.error('Error calling API:', error);
        this.errorMessage = 'Failed to get prediction. Check if the FastAPI backend is running.';
        this.isLoading = false;
      }
    });
  }
}
