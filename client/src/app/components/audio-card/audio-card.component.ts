import { Component, OnInit, Input } from '@angular/core';
import { Audiobook } from '../../model/audiobook';
@Component({
  selector: 'app-audio-card',
  templateUrl: './audio-card.component.html',
  styleUrls: ['./audio-card.component.scss']
})
export class AudioCardComponent implements OnInit {

  @Input()
  private audiobook: Audiobook;

  constructor() {
   }

  ngOnInit() {
    console.log(this.audiobook);
  }
}
