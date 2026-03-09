<script>
  import { supabase } from '$lib/supabase';
  let status = { isPaused: false };

  onMount(() => {
    supabase
      .channel('pause-state')
      .on('postgres_changes', { event: '*', schema: 'public', table: 'pause_state' }, payload => {
        status = payload.new;
      })
      .subscribe();
  });
</script>
