import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LibraryTabComponent } from './library-tab.component';

describe('LibraryTabComponent', () => {
  let component: LibraryTabComponent;
  let fixture: ComponentFixture<LibraryTabComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LibraryTabComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LibraryTabComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
