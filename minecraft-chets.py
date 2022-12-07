       POINT aCenterPos,bCenterPos;          
	CSquare whiteSquare,blackSquare;
	int i,j;

	aCenterPos.x = 100;                                        //wspolrzedne x
	aCenterPos.y = 100;
	whiteSquare.SetCenterPos(aCenterPos);            //pobranie wspolrzednych
	whiteSquare.SetPenColor(RGB(0,0,0));             //kolor obramowania
	whiteSquare.SetFillColor(RGB(255,255,255));   //kolor wypelnienia
	whiteSquare.SetPenWidth(2);                          //grubosc obramowania
	

	aCenterPos.x = 200;
	aCenterPos.y = 100;
	blackSquare.SetCenterPos(aCenterPos);
	blackSquare.SetPenColor(RGB(0,0,0));
	blackSquare.SetFillColor(RGB(0,0,0));
	blackSquare.SetPenWidth(2);
	

	for(i=0;i<8;i++)
	{
		for(j=0;j<8;j++)
			if((i + j)%2 == 0)                     //pola parzyste, nieparzyste warunek
				blackSquare.Paint(hdc);     //rysowanie czarnego kwadratu
				
			else
				whiteSquare.Paint(hdc);    //rysowanie bialego kwadratu
				
			}