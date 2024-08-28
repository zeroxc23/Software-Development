import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-games',
  standalone: true,
  imports: [CommonModule],
  template:`
  <ul>
    @for (game of games; track game.id){
      <li>{{ game.name }}</li>
    }
  </ul>
  `,
  styleUrl: './games.component.css'
})
export class GamesComponent {
  games=[{
    "id": 1,
    "name": "Game1",
    "description": "Game1 description",
  },
  {
    "id": 2,
    "name": "Game2",
    "description": "Game2 description",

  },
  {
    "id": 3,
    "name": "Game3",
    "description": "Game3 description",
  }
  
]
}
