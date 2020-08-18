/////////////////////////////////////////////////////////////////////////////
// INTEGRITY INSTRUCTIONS (v2)

// Explicitly state the level of collaboration on this question
// Examples:
//   * I discussed ideas with classmate(s) [include name(s)]
//   * I worked together with classmate(s) in the lab [include name(s)]
//   * Classmate [include name] helped me debug my code
//   * I consulted website [include url]
//   * None
//
// A "None" indicates you completed this question entirely by yourself
// (or with assistance from course staff, which you do not have to mention)
/////////////////////////////////////////////////////////////////////////////
// INTEGRITY STATEMENT:
// I received help from and/or collaborated with: None


// Name: Harman Singh
// login ID: h286sing
/////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////
// PROVIDED FUNCTION and CONSTANTS (DO NOT CHANGE)

// print_header(year, month) prints the calendar "header"
//   for the given year/month
// notes:   if month is invalid, does not print full header
//          header is best aligned for 4-digit years
// effects: produces output

#include <stdbool.h>
#include <stdio.h>


void print_header(int year, int month) {
  if (month == 1) {
    printf("====January %d====\n", year);
  } else if (month == 2) {
    printf("===February %d====\n", year);
  } else if (month == 3) {
    printf("=====March %d=====\n", year);
  } else if (month == 4) {
    printf("=====April %d=====\n", year);
  } else if (month == 5) {
    printf("======May %d======\n", year);
  } else if (month == 6) {
    printf("=====June %d======\n", year);
  } else if (month == 7) {
    printf("=====July %d======\n", year);
  }else if (month == 8) {
    printf("====August %d=====\n", year);
  } else if (month == 9) {
    printf("===September %d===\n", year);
  } else if (month == 10) {
    printf("====October %d====\n", year);
  } else if (month == 11) {
    printf("===November %d====\n", year);
  } else if (month == 12) {
    printf("===December %d====\n", year);
  }
  printf("Su Mo Tu We Th Fr Sa\n");
}

const int base_year = 1589;
const int SUNDAY = 0;
const int base_year_jan_1 = SUNDAY;

/////////////////////////////////////////////////////////////////////////////

// is_leap_year(year) determines if the year is a leap year
// requires: year is greater than or equal to 1589
bool is_leap_year(int year) {
//   assert(year >= 1589);
  if(year % 100 == 0) {
    if(year % 400 == 0) {
      return true;
    }
    else {
      return false;
    }
  }
  else if(year % 4 == 0) {
    return true;
  }
  else {
    return false;
  }
}

// days_in_month(year, month) returns number of dates in that month of
// a particular year.
// requires: year is greater than or equal to 1589
int days_in_month(int year, int month) {
//   assert(year >= 1589);
  if(month == 1) {
    return 31;
  }
  else if(month == 2) {
    int february = 0;
    if(is_leap_year(year)) {
      february = 29;
    }
    else {
      february = 28;
    }
    return february;
  }
  else if(month == 3) {
    return 31;
  }
  else if(month == 4) {
    return 30;
  }
  else if(month == 5) {
    return 31;
  }
  else if(month == 6) {
    return 30;
  }
  else if(month == 7) {
    return 31;
  }
  else if(month == 8) {
    return 31;
  }
  else if(month == 9) {
    return 30;
  }
  else if(month == 10) {
    return 31;
  }
  else if(month == 11) {
    return 30;
  }
  else if(month == 12) {
    return 31;
  }
  else {
    return 0;
  }
}

// days_of_the_week(year, month, day) finds the "day of the week" 
// for the given date
// effects: modify current_date, current_month, current_year
// requires: year is greater than or equal to 1589
int day_of_the_week(int year, int month, int day) {
//   assert(year >= 1589);
  int current_day = 0;
  for(int current_year = base_year; current_year <= year; current_year++) {
    for(int current_month = 1; current_month <= 12; current_month++) {
      if(current_month == month && current_year == year) {
        current_day += day - 1;
        break;
      }
      else {
        current_day += days_in_month(current_year, current_month);
      }
    }
  }
  return current_day % 7;
}

// print_calendar(year, month) prints a calendar for a given month.
// requires: year is greater than or equal to 1589
// effects: produce output
//          modify current_week, period, current_date
void print_calendar(int year, int month) {
  print_header(year, month);
  int period = 0;
  for(int current_week = 0;
      current_week < day_of_the_week(year, month, 1); 
      current_week ++) {
    printf("   ");
    period += 1;
  }
  for(int current_date = 1; current_date <= days_in_month(year, month);
      current_date++) {
    if(day_of_the_week(year, month, current_date) == 6 || 
       current_date == days_in_month(year, month)) {
      printf("%2d",current_date);
    }
    else {
      printf("%2d ",current_date);
    }
    period ++;
    if(period == 7) {
      printf("\n");
      period = 0;
    }
  }
  printf("\n");
}


int main(void) {
  print_calendar(2001, 5);
}
