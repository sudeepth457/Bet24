<script type="text/javascript">
function increment() {
  val = document.getElementById("number").value;
  v={{ava_vote}}
  a={{ current_match.votes }}
  if(val<a)
  {
     val++;
     document.getElementById("number").value=val;
  }
}
function decrement() {
  val = document.getElementById("number").value;
  v={{ava_vote}}
  a={{ current_match.votes }}
  if(val>0)
  {
     val--;
     document.getElementById("number").value=val;
  }
}
</script>


