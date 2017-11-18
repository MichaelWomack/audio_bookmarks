import { Component, OnInit, Input } from '@angular/core';
import { AudioInfo } from './../../model/audio-info';
@Component({
  selector: 'app-audio-card',
  templateUrl: './audio-card.component.html',
  styleUrls: ['./audio-card.component.scss']
})
export class AudioCardComponent implements OnInit {

  @Input()
  private audioInfo: AudioInfo;

  constructor() {
    console.log(this.audioInfo);
   }

  ngOnInit() {
  }
}
