public static void simetrik_fark(int[] a ,int[] b){
    int uzunluk = a.length;
    int[] birleim = new int[uzunluk];
    for ( int i = 0 ; i<a.length;i++){
        if(i<a.length){
            int eleman = a[i];
            for(int j = 0 ; j<b.length;j++){
                if (eleman == b[j]) {
                    birleim[i] = eleman;
                }
            }
        }
    }

}