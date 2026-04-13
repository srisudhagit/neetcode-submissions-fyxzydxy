/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
        List<Interval> schedule = new ArrayList<>();
        int schLen = -1;
        intervals.sort((a, b) -> a.start - b.start);
        for(int i=0;i<intervals.size();i++){
            Interval current = intervals.get(i);
            if(!schedule.isEmpty()){
                Interval intvl = schedule.get(schLen);
                if(intvl.end > current.start){
                    return false;
                }
            }
            schedule.add(current);
            schLen++;
        }
        return true;
    }
}
